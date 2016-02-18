import file_io
import source_code_extractor
from CodeforcesImporter.classifier import template_generator
from CodeforcesImporter.classifier.classifier import Classifier

from submission_importer import SubmissionImport


def import_codes(handle, dir_path='.\log\\'):
    try:
        importer = SubmissionImport(handle)
        try:
            submissions_list = importer.get_submissions()

            if submissions_list is not None:
                classifier = Classifier()
                for submission in submissions_list:
                    try:
                        log_submission(submission)

                        code = source_code_extractor.extract_source_code(str(submission.contest_id), str(submission.id));

                        problem_id = str(submission.contest_id) + submission.problem.index
                        problem_name = submission.problem.name
                        problem_name = resolve(problem_name);

                        path = dir_path + '\\' + problem_id + '-' + problem_name + '.txt'

                        # adding problem to classifier
                        classifier.add_to_classifier(submission.problem, submission.id, path);

                        # writing submission to file
                        file_io.write_to_file(path, code);

                        print 'Successfully written submission: ' + str(submission.id) + ' to ' + path
                        print ''

                    except Exception as ex:
                        print ex

                print dir_path
                template_generator.generate_html(classifier, dir_path)

        except TypeError as ex:
            print ex
        except Exception as ex:
            raise ex
    except Exception as ex:
        print 'Error: ' + ex.errno
        print 'Unable to fetch your submissions at the moment'
    else:
        print 'Import-Status: Successful'


def resolve(problem_name):
    problem_name = problem_name.replace('/', '').replace('\\', '').replace(' ', '_');
    return problem_name


def log_submission(submission):
    print "[",
    print 'id = ' + str(submission.contest_id) + submission.problem.index + ', ',
    print 'name = ' + submission.problem.name + ', ',
    print 'verdict = ' + submission.verdict + ', ',
    print 'submission_id=' + str(submission.id),
    print "]"