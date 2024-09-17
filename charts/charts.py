import matplotlib.pyplot as plt

def generate_pie_charts():
    values = [200, 34, 120]
    labels = ['A', 'B', 'C']
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()