from matplotlib import pyplot
#1. Prepare data
machine_counts = [18, 4, 2]
#2. Prepare label
machine_names = ["PC", "Mac", "Linux"]
#3. Draw pie
pyplot.pie(machine_counts, labels=machine_names, autopct="%.1f%%", shadow=True, explode= [0, 0.1, 0])
pyplot.title("PC vs Mac vs Linux usage")
pyplot.axis("equal")
#4. Show
pyplot.show()