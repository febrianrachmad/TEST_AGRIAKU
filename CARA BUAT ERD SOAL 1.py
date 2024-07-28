import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_erd():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Entities
    entities = {
        'Student': (2, 8),
        'Enrollment': (6, 8),
        'Schedule': (10, 8),
        'Course': (10, 5),
        'Lecturer': (10, 2),
        'Course_Attendance': (6, 5)
    }

    for entity, pos in entities.items():
        ax.add_patch(mpatches.FancyBboxPatch(
            (pos[0] - 1.5, pos[1] - 0.5), 3, 1,
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"
        ))
        ax.text(pos[0], pos[1], entity, ha='center', va='center', fontsize=12)

    # Relationships
    relationships = [
        ('Student', 'Enrollment'),
        ('Enrollment', 'Schedule'),
        ('Schedule', 'Course'),
        ('Schedule', 'Lecturer'),
        ('Student', 'Course_Attendance'),
        ('Course_Attendance', 'Schedule')
    ]

    for start, end in relationships:
        start_pos = entities[start]
        end_pos = entities[end]
        ax.annotate("",
            xy=(end_pos[0], end_pos[1]), xycoords='data',
            xytext=(start_pos[0], start_pos[1]), textcoords='data',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.3", color='black')
        )

    # Attributes
    attributes = {
        'Student': ['STUDENT_ID'],
        'Enrollment': ['ENROLL_ID', 'STUDENT_ID', 'SCHEDULE_ID', 'ACADEMIC_YEAR', 'SEMESTER', 'ENROLL_DT'],
        'Schedule': ['SCHEDULE_ID', 'COURSE_ID', 'LECTURER_ID', 'START_DT', 'END_DT', 'COURSE_DAYS'],
        'Course': ['COURSE_ID', 'NAME'],
        'Lecturer': ['LECTURER_ID'],
        'Course_Attendance': ['ATTENDANCE_ID', 'STUDENT_ID', 'SCHEDULE_ID', 'ATTEND_DT']
    }

    for entity, attr_list in attributes.items():
        pos = entities[entity]
        for i, attr in enumerate(attr_list):
            ax.text(pos[0], pos[1] - 0.3 * (i + 1), attr, ha='center', va='top', fontsize=10, color='black')

    plt.show()

draw_erd()
