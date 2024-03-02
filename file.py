def solution(queries):
    storage = {}  # Dictionary to hold file names, sizes, and owner
    users = {"admin": {"capacity": float('inf'), "used": 0}}  # Admin with unlimited capacity
    backups = {}  # Dictionary for user backups
    response = []

    for q in queries:
        command = q[0]

        if command == "ADD_USER":
            userId, capacity = q[1], int(q[2])
            if userId in users:
                response.append("false")
            else:
                users[userId] = {"capacity": capacity, "used": 0}
                response.append("true")

        elif command == "ADD_FILE":
            userId = "admin"
            name, size = q[1], int(q[2])
            if name in storage:
                response.append("false")
            else:
                storage[name] = {"size": size, "owner": userId}
                response.append("true")

        elif command == "ADD_FILE_BY":
            userId, name, size = q[1], q[2], int(q[3])
            if userId not in users or name in storage or users[userId]["used"] + size > users[userId]["capacity"]:
                response.append("")
            else:
                storage[name] = {"size": size, "owner": userId}
                users[userId]["used"] += size
                response.append(str(users[userId]["capacity"] - users[userId]["used"]))

        elif command == "GET_FILE_SIZE":
            name = q[1]
            if name in storage:
                response.append(str(storage[name]["size"]))
            else:
                response.append("")

        elif command == "DELETE_FILE":
            name = q[1]
            if name in storage:
                fileSize = storage[name]["size"]
                userId = storage[name]["owner"]
                users[userId]["used"] -= fileSize
                del storage[name]
                response.append(str(fileSize))
            else:
                response.append("")

        elif command == "BACKUP_USER":
            userId = q[1]
            if userId in users:
                backups[userId] = {name: storage[name]["size"] for name in storage if storage[name]["owner"] == userId}
                response.append(str(len(backups[userId])))
            else:
                response.append("")

        elif command == "RESTORE_USER":
            userId = q[1]
            if userId in users:
                # Delete current files of the user
                for name in list(storage.keys()):
                    if storage[name]["owner"] == userId:
                        del storage[name]
                        users[userId]["used"] = 0  # Reset used capacity

                restored_count = 0
                if userId in backups:
                    for name, size in backups[userId].items():
                        # Ensure no name conflict and respect user's capacity
                        if name not in storage:
                            storage[name] = {"size": size, "owner": userId}
                            users[userId]["used"] += size
                            restored_count += 1
                response.append(str(restored_count))
            else:
                response.append("")

    return response

# Example input
queries = [
    ["ADD_USER", "user", "40"], 
    ["BACKUP_USER", "user"], 
    ["ADD_FILE_BY", "user", "/dir/file.txt", "30"], 
    ["ADD_FILE_BY", "user", "/dir/file.mp4", "10"], 
    ["RESTORE_USER", "user"], 
    ["GET_FILE_SIZE", "/dir/file.txt"]
]

# Run the solution with the example input
output = solution(queries)
print(output)
