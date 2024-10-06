from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="1.2",
    description="A CLI for tracking your tasks and managing your to-dos for you",
    packages= find_packages(),
    entry_points=
    {
        'console_scripts':[
            'task-tracker=modules.task_tracker:main',
        ],
        
    },
)