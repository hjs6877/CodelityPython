class FrogJump:
    def __init__(self):
        print("객체 생성")

    def solution(self, x, y, d):
        quotient = (y - x) // d
        remainder = (y - x) % d

        if remainder == 0:
            count = quotient
        else:
            count = quotient + 1

        return count


if __name__ == "__main__":
    x1 = 40
    y1 = 190
    d1 = 35
    frog_jump = FrogJump()
    result = frog_jump.solution(x1, y1, d1)
    print(result)



