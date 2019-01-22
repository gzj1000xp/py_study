from matplotlib import pyplot as plt


def bar():
    past_years_averages = [82, 84, 83, 86, 74, 84, 90]
    years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
    error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

    # Make your chart here
    plt.figure(figsize=(10, 8))
    plt.bar(range(len(years)), past_years_averages, yerr=error, capsize=5)
    ax = plt.subplot()
    ax.axis([-0.5, 6.5, 70, 95])
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years)
    plt.title('Final Exam Averages')
    plt.xlabel('Year')
    plt.ylabel('Test average')
    plt.savefig('my_bar_chart.png')

    plt.show()


def bar_side():
    unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
    middle_school_a = [80, 85, 84, 83, 86]
    middle_school_b = [73, 78, 77, 82, 86]

    def create_x(t, w, n, d):
        return [t * x + w * n for x in range(d)]

    school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
    school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
    # Make your chart here
    x_a = create_x(2, 0.8, 1, 5)
    x_b = create_x(2, 0.8, 2, 5)

    plt.figure(figsize=(10, 8))
    ax = plt.subplot()
    plt.bar(x_a, middle_school_a, label="Middle School A")
    plt.bar(x_b, middle_school_b, label="Middle School B")
    plt.legend()

    plt.title("Test Averages on Different Units")
    plt.xlabel("Unit")
    plt.ylabel("Test Average")

    middle_x = [(a + b) / 2 for a, b in zip(school_a_x, school_b_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(unit_topics)

    plt.savefig("my_side_by_side.png")
    plt.show()

