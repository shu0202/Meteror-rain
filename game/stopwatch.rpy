init python:
    intervalCounter = 0
    value = 0

    def myTimer():
        store.intervalCounter += 1
        if intervalCounter < 20: return
        store.intervalCounter = 0
        store.value += 1
        renpy.restart_interaction()
