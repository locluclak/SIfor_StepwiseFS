import scipy 
import matplotlib.pyplot as plt

def count_floats_less_equal(file_path, threshold=0.05):
    count = 0
    ls = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                num = float(line.strip())  # Convert the line to a float
                ls.append(num)
                if num > 1:
                    print(ls[-2])
                if num <= threshold:
                    count += 1
            except ValueError:
                continue
    return count, ls

file_path = 'Experiment/Listpvalue_para_fixed_150_5.txt'  
result,ls = count_floats_less_equal(file_path)
print(f"Number of floats less than or equal to 0.05: {result}")
print("FPR:",result / len(ls))
print(f"Quantity{len(ls)}")
kstest_pvalue = scipy.stats.kstest(ls, 'uniform').pvalue
print('Uniform Kstest check:', kstest_pvalue)
plt.hist(ls)
# Save the histogram
plt.savefig('uniform_hist.png')
plt.show()