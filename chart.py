import matplotlib.pyplot as plt

# Data
topics = [
    "1.1 x", "1.2 xx", "1.3 xxx",
    "2.1 y",
    "3.1 z", "zz",
]
counts = [
    151, 88, 12, #Insert the values from main.py
    145,
    106, 42,
]

plt.figure(figsize=(10, 6))
plt.barh(topics, counts, color='#133337')
plt.xlabel('Questions')
plt.ylabel('Topics')
plt.title('Number of questions per topic')
plt.tight_layout()

plt.show()
