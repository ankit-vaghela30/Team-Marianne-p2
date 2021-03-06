
import argparse
import src.__main__

def main():
    parser = argparse.ArgumentParser(description='Team Marianne solution for Malware Classification')

    # All args are optional. Default values are set for each argument
    parser.add_argument ("-d", "--dataset", default="data/sample/X_vs_train.txt",
        help = "Path to text file containing hash of documents in training set")

    parser.add_argument ("-l", "--labels", default="data/sample/y_vs_train.txt",
        help = "Path to text file containing labels of documents in training set")

    parser.add_argument ("-t", "--testset", default="data/sample/X_vs_test.txt",
        help = "Path to text file containing hash of documents in testing set")

    parser.add_argument ("-e", "--evaluate", action="store_true",
        help = "Set this to evaluate accuracy on the test set")

<<<<<<< HEAD
    parser.add_argument ("-m", "--testlabels", default="data/sample/y_vs_test.txt",
        help = "Path to text file containing labels of documents in testing set."
                "If evaluate is set true, this file is compared with classifier output")
parser.add_argument ("-m", "--testlabels",
    help = "Path to text file containing labels of documents in testing set."
            "If evaluate is set true, this file is compared with classifier output")
>>>>>>> 286f8e4792d60fbb1c5f01c683026c32cadb49c9

    parser.add_argument ("-a", "--asmtrain", default="data/sample/TrainAsm/",
        help = "Path to directory that contains asm documemts of training set")

    parser.add_argument ("-at", "--asmtest", default="data/sample/TestAsm/",
        help = "Path to directory that contains asm documemts of testing set")

    parser.add_argument ("-b", "--bytestrain", default="data/sample/TrainBytes/",
        help = "Path to directory that contains bytes documemts of training set")

    parser.add_argument ("-bt", "--bytestest", default="data/sample/TestBytes/",
        help = "Path to directory that contains bytes documemts of testing set")

    parser.add_argument ("-A", "--asmrdd", default="data/sample/asm_rdd.txt",
        help = "Path to text file in which RDD from asm file is stored after preprocessing")

    parser.add_argument ("-B", "--bytesrdd", default="data/sample/bytes_rdd.txt",
        help = "Path to text file in which RDD from bytes file is stored after preprocessing")

<<<<<<< HEAD
    parser.add_argument ("-o", "--output", default="output",
        help = "Path to the directory where output will be written")

    args = parser.parse_args()

    src.__main__.main(args)
parser.add_argument ("-C", "--bytesrddTest", default="data/sample/bytes_rdd_test.txt",
    help = "Path to text file in which RDD from bytes file is stored after preprocessing for test")

parser.add_argument ("-o", "--output", default="data/sample/output.txt",
    help = "Path to the directory where output will be written")

parser.add_argument ("-model", "--mlModel", default="rf",
    help = "Specifies which ML model is to be used")

args = parser.parse_args()

src.__main__.main(args)
>>>>>>> 286f8e4792d60fbb1c5f01c683026c32cadb49c9
