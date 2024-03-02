# test.py
from file import solution

def test_case_1():
    queries = [
        ["ADD_USER", "user1", "100"],
        ["ADD_FILE_BY", "user1", "/file1.txt", "60"],
        ["GET_FILE_SIZE", "/file1.txt"],
        ["DELETE_FILE", "/file1.txt"],
        ["GET_FILE_SIZE", "/file1.txt"]
    ]
    expected_output = ["true", "40", "60", "60", ""]
    output = solution(queries)
    assert output == expected_output, f"Test Case 1 Failed: Expected {expected_output}, got {output}"
    print("Test Case 1 Passed")

def test_case_2():
    queries = [
        ["ADD_USER", "user2", "50"],
        ["ADD_FILE_BY", "user2", "/config.json", "20"],
        ["BACKUP_USER", "user2"],
        ["DELETE_FILE", "/config.json"],
        ["RESTORE_USER", "user2"],
        ["GET_FILE_SIZE", "/config.json"]
    ]
    expected_output = ["true", "30", "1", "20", "1", "20"]
    output = solution(queries)
    assert output == expected_output, f"Test Case 2 Failed: Expected {expected_output}, got {output}"
    print("Test Case 2 Passed")

def test_case_3():
    # Test adding a user and exceeding the storage limit
    queries = [
        ["ADD_USER", "user3", "30"],
        ["ADD_FILE_BY", "user3", "/largefile.mp4", "31"],
    ]
    expected_output = ["true", ""]
    output = solution(queries)
    assert output == expected_output, f"Test Case 3 Failed: Expected {expected_output}, got {output}"
    print("Test Case 3 Passed")

def test_case_4():
    # Test restoring when another user has a file with the same name
    queries = [
        ["ADD_USER", "user4", "100"],
        ["ADD_USER", "user5", "50"],
        ["ADD_FILE_BY", "user4", "/sharedfile.txt", "20"],
        ["BACKUP_USER", "user4"],
        ["DELETE_FILE", "/sharedfile.txt"],
        ["ADD_FILE_BY", "user5", "/sharedfile.txt", "20"],
        ["RESTORE_USER", "user4"],
    ]
    expected_output = ["true", "true", "80", "1", "20", "30", "0"]
    output = solution(queries)
    assert output == expected_output, f"Test Case 4 Failed: Expected {expected_output}, got {output}"
    print("Test Case 4 Passed")

def test_case_5():
    # Test backup and restore with multiple files and partial restoration due to capacity
    queries = [
        ["ADD_USER", "user6", "60"],
        ["ADD_FILE_BY", "user6", "/fileA.txt", "20"],
        ["ADD_FILE_BY", "user6", "/fileB.txt", "30"],
        ["BACKUP_USER", "user6"],
        ["DELETE_FILE", "/fileA.txt"],
        ["DELETE_FILE", "/fileB.txt"],
        ["ADD_FILE_BY", "user6", "/fileC.txt", "50"],
    ]
    expected_output = ["true", "40", "10", "2", "20", "30", "10"]
    output = solution(queries)
    assert output == expected_output, f"Test Case 5 Failed: Expected {expected_output}, got {output}"
    print("Test Case 5 Passed")

def test_case_6():
    # Test operations with a non-existent user
    queries = [
        ["ADD_USER", "user7", "100"],
        ["BACKUP_USER", "user8"],  # User does not exist
        ["RESTORE_USER", "user8"],  # User does not exist
        ["ADD_FILE_BY", "user8", "/file.txt", "10"],  # User does not exist
    ]
    expected_output = ["true", "", "", ""]
    output = solution(queries)
    assert output == expected_output, f"Test Case 6 Failed: Expected {expected_output}, got {output}"
    print("Test Case 6 Passed")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    print("All tests passed!")

