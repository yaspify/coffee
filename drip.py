# drip_coffee.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Drip coffee calculation")
    parser.add_argument("-b", "--bean", type=float, required=True,
                        help="Amount of coffee beans (g)")
    parser.add_argument("-r", "--watercoffeeratio", type=float, required=True,
                        help="Water-to-coffee ratio")
    args = parser.parse_args()

    bean = args.bean
    ratio = args.watercoffeeratio

    step1 = bean * 2
    step2 = bean * ratio * 0.4
    step3 = step2 + bean * ratio * 0.2
    step4 = step2 + bean * ratio * 0.4
    step5 = bean * ratio

    print(f"(1) {int(step1)}")
    print(f"(2) {int(step2)}")
    print(f"(3) {int(step3)}")
    print(f"(4) {int(step4)}")
    print(f"(5) {int(step5)}")

if __name__ == "__main__":
    main()
