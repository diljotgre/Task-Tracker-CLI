from setuptools import setup 

setup(
    name="task-tracker",
    version="0.3",
    description="A CLI for tracking your tasks and managing your to-dos for you",
    py_modules=['task_tracker'],
    entry_points=
    {
        'console_scripts':[
            'task-tracker=task_tracker:main',
        ],
        
    },
)