
TEXT = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''

TEXT2 = '''It's flying from somewhere
As fast as it can
I couldn't keep up with it
Not if I ran'''

TEXT3 = '''And the Raven never flitting still is sitting still is sitting
On the pallid bust of Pallas just above my chamber door
And his eyes have all the seeming of a demon’s that is dreaming
And the lamp-light o’er him streaming throws his shadow on the floor
And my soul from out that shadow that lies floating on the floor
Shall be lifted nevermore'''

TEXT4 = '''I will go to the cinema
No you will not'''

TESTS = {
    "Basics": [
        {
            "input": [TEXT, ['i', 'was', 'three', 'near']],
            "answer": {
                'i': 4,
                'was': 3,
                'three': 0,
                'near': 0
            }
        }
    ],
    "Extra": [
        {
            "input": [TEXT, ['one', 'two', 'three']],
            "answer": {
                'one': 1,
                'two': 1,
                'three': 0
            }
        },
        {
            "input": [TEXT2, ["it's", "ran", "i"]],
            "answer": {
                "it's": 1,
                "ran": 1,
                "i": 2
            }
        },
        {
            "input": [TEXT3, ["raven", "still", "is", "floor", "nevermore"]],
            "answer": {
                'raven': 1,
                'still': 2,
                'is': 3,
                'floor': 2,
                'nevermore': 1
            }
        },
        {
            "input": [TEXT4, ["i", "will", "no"]],
            "answer": {
                "i": 1,
                "will": 2,
                "no": 1
            }
        }
    ]
}
