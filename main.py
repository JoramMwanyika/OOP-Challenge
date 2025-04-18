from pet import Pet

def main():
    # Create a new pet
    print("Creating pet: Max")
    max = Pet("Max")
    
    # Test basic actions
    max.eat()
    max.play()
    max.sleep()
    
    # Teach some tricks
    max.train("roll over")
    max.train("play dead")
    
    # Show current status
    max.get_status()
    
    # Show learned tricks
    max.show_tricks()

if __name__ == "__main__":
    main() 