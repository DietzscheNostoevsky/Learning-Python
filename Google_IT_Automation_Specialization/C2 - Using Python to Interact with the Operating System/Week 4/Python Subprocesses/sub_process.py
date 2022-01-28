import subprocess

# subprocess.run(["date"])

#subprocess.run(["sleep", "2"])

result = subprocess.run(["host", '8.8.8.8'], capture_output=True)
print(result, "\n")
print(result.stdout, "\n")

print(result.stdout.decode().split())
