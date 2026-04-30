from pyspark import SparkContext

sc = SparkContext("local", "MatrixMultiplication")

data = sc.textFile("matrix.txt")

lines = data.map(lambda line: line.split(","))

def mapper(record):
    matrix, i, j, value = record
    i = int(i)
    j = int(j)
    value = int(value)

    if matrix == "A":
        for k in range(2):
            yield ((i, k), ("A", j, value))
    else:
        for k in range(2):
            yield ((k, j), ("B", i, value))

mapped = lines.flatMap(mapper)

grouped = mapped.groupByKey()

def reducer(values):
    A = {}
    B = {}

    for val in values:
        if val[0] == "A":
            A[val[1]] = val[2]
        else:
            B[val[1]] = val[2]

    result = 0
    for key in A:
        if key in B:
            result += A[key] * B[key]

    return result

result = grouped.map(lambda x: (x[0], reducer(x[1])))

for r in result.collect():
    print(r)

sc.stop()
