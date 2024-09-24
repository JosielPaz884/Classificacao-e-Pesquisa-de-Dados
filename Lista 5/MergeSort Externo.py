import os
import tempfile

def externalMergesort(inputFile, outputFile, chunkSize=1024):
    tempDir = tempfile.mkdtemp()
    chunks = []
    with open(inputFile, 'r') as f:
        while True:
            chunk = f.read(chunkSize)
            if not chunk:
                break
            chunks.append(chunk)
    sortedChunks = []
    for chunk in chunks:
        with tempfile.NamedTemporaryFile(dir=tempDir, delete=False) as tmp:
            tmp.write(chunk.encode())
            tmp.flush()
            sortedChunk = sortChunk(tmp.name)
            sortedChunks.append(sortedChunk)
    with open(outputFile, 'w') as f:
        while sortedChunks:
            minChunk = min(sortedChunks, key=lambda x: x[0])
            f.write(minChunk[1])
            sortedChunks.remove(minChunk)
    for file in os.listdir(tempDir):
        os.remove(os.path.join(tempDir, file))
    os.rmdir(tempDir)

def sortChunk(chunkFile):
    with open(chunkFile, 'r') as f:
        chunk = f.read()
    sortedChunk = mergesort(chunk.splitlines())
    return (sortedChunk[0], '\n'.join(sortedChunk))

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

externalMergesort('input.txt', 'output.txt')
