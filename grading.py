from rubrics.Exercise1Rubric import buildExercise1Rubric
from rubrics.Exercise2Rubric import buildExercise2Rubric
from rubrics.Exercise3Rubric import buildExercise3Rubric
from rubrics.Exercise4Rubric import buildExercise4Rubric
from rubrics.Exercise5Rubric import buildExercise5Rubric
import os
import sys


def gradeExercise(
    exNumber, rubricFactory, expectedModels, expectedOutputFile, expectedOutputTable
):
    print(f"[INFO] Preparing feedback for EXERCISE {exNumber}:")
    print(
        "[INFO] If this exercise does not need to be submitted yet, you can ignore all output after this."
    )
    if os.path.isfile(expectedOutputFile):
        os.remove(expectedOutputFile)

    for expectedModel in expectedModels:
        print(f"\tLooking for {expectedModel} to execute.")
        if os.path.isfile(expectedModel):
            print(f"\t[SUCCESS] Found {expectedModel}, executing.")
            if expectedModel.endswith(".py"):
                os.system(f"python {expectedModel}")
                break
            elif expectedModel.endswith(".jv"):
                os.system(f"jv {expectedModel}")
                break
            else:
                print(
                    f"\t[INFO] Could not find interpreter for model: {expectedModel}."
                )
                print("\tSkipping.")
                return

    print(f"\tLooking for {expectedOutputFile} to grade.")
    if os.path.isfile(expectedOutputFile):
        print(f"\t[SUCCESS] Found output file {expectedOutputFile}, grading...")
    else:
        print(f"\t[ERROR] Can not find expected output file: {expectedOutputFile}.")
        print("\tMake sure your model generates it as described in the exercise!")
        print("\tSkipping.")
        return

    feedback = (
        rubricFactory()
        .gradeData("sqlite:///{}".format(expectedOutputFile), expectedOutputTable)
        .getConsoleOutput()
    )

    print("")
    print(feedback)


if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

gradeExercise(
    1,
    buildExercise1Rubric,
    ["exercises/exercise1.py", "exercises/exercise1.jv"],
    "airports.sqlite",
    "airports",
)
gradeExercise(
    2,
    buildExercise2Rubric,
    ["exercises/exercise2.py", "exercises/exercise2.jv"],
    "trainstops.sqlite",
    "trainstops",
)
gradeExercise(
    3,
    buildExercise3Rubric,
    ["exercises/exercise3.py", "exercises/exercise3.jv"],
    "cars.sqlite",
    "cars",
)
gradeExercise(
    4,
    buildExercise4Rubric,
    ["exercises/exercise4.py", "exercises/exercise4.jv"],
    "temperatures.sqlite",
    "temperatures",
)
gradeExercise(
    5,
    buildExercise5Rubric,
    ["exercises/exercise5.py", "exercises/exercise5.jv"],
    "gtfs.sqlite",
    "stops",
)
