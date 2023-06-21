import subprocess

def count_files(directory: list) -> int:
    result = subprocess.run(['find', directory, '-type', 'f', '-print'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    file_list = result.stdout.splitlines()
    return len(file_list)



def calculate_weights(directories: list) -> (list):
    result_weights = []
    total_weight = 0
    for directory in directories:
        result_weight = subprocess.run(['du', '-shc', directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        result_weights.append(result_weight)
        output = result_weight.stdout.strip()
        if output:
            weight = output.split()[0]
            if weight.isdigit():
                total_weight += int(weight)
    return result_weights, total_weight



def main():
    directories = input("Podaj ścieżki do katalogów oddzielone przecinkiem: ").split(",")
    file_counts = [count_files(directory) for directory in directories]
    weights, total_weight = calculate_weights(directories)
    output_file = open("output.txt", "w")
    for i, directory in enumerate(directories):
        print(f"Ilość plików w katalogu '{directory}': {file_counts[i]}", file=output_file)
        output = weights[i].stdout.strip()
        print(f"Waga katalogu '{directory}': {output}", file=output_file)
    print(f"Suma wag wszystkich katalogów: {total_weight}", file=output_file)
    output_file.close()


main()
