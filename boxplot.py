Test 1: 80
Test 2: 85
Test 3: 83
Test 4: 87
Test 5: 86 
import matplotlib.pyplot as plt

cycle_tests = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
marks = [80, 75, 85, 90, 70]

plt.bar(cycle_tests, marks)
plt.xlabel('Cycle Tests')
plt.ylabel('Marks')
plt.title('Marks in Cycle Tests')

plt.show()
