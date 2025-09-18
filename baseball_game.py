#!/usr/bin/env python3
"""
Baseball Game Simulation
A simple text-based baseball game where you can play against the computer.
"""

import random
import time

class BaseballGame:
    def __init__(self):
        self.home_score = 0
        self.away_score = 0
        self.inning = 1
        self.top_bottom = "Top"  # Top = Away team bats, Bottom = Home team bats
        self.outs = 0
        self.bases = [False, False, False]  # [1st, 2nd, 3rd]
        self.game_over = False
        
    def print_scoreboard(self):
        """Print the current scoreboard"""
        print("\n" + "="*50)
        print(f"INNING: {self.inning} {self.top_bottom}")
        print(f"OUTS: {self.outs}")
        print(f"SCORE: Away {self.away_score} - Home {self.home_score}")
        print(f"BASES: 1st: {'X' if self.bases[0] else 'O'} 2nd: {'X' if self.bases[1] else 'O'} 3rd: {'X' if self.bases[2] else 'O'}")
        print("="*50)
    
    def get_batting_result(self):
        """Simulate a batting result"""
        outcomes = [
            ("Single", 0.3),
            ("Double", 0.15),
            ("Triple", 0.05),
            ("Home Run", 0.1),
            ("Walk", 0.15),
            ("Strikeout", 0.15),
            ("Groundout", 0.05),
            ("Flyout", 0.05)
        ]
        
        rand = random.random()
        cumulative = 0
        for outcome, probability in outcomes:
            cumulative += probability
            if rand <= cumulative:
                return outcome
        return "Groundout"
    
    def advance_runners(self, bases_advanced):
        """Advance runners on the bases"""
        runs_scored = 0
        
        # Move runners
        for i in range(len(self.bases) - 1, -1, -1):
            if self.bases[i]:
                new_position = i + bases_advanced
                if new_position >= 3:
                    runs_scored += 1
                else:
                    self.bases[new_position] = True
                self.bases[i] = False
        
        return runs_scored
    
    def handle_batting_result(self, result):
        """Handle the result of a batting attempt"""
        print(f"Result: {result}")
        
        if result == "Strikeout" or result == "Groundout" or result == "Flyout":
            self.outs += 1
            if self.outs >= 3:
                self.end_half_inning()
        elif result == "Single":
            runs = self.advance_runners(1)
            self.bases[0] = True
            self.add_runs(runs)
        elif result == "Double":
            runs = self.advance_runners(2)
            self.bases[1] = True
            self.add_runs(runs)
        elif result == "Triple":
            runs = self.advance_runners(3)
            self.bases[2] = True
            self.add_runs(runs)
        elif result == "Home Run":
            runs = self.advance_runners(3) + 1  # Batter scores too
            self.add_runs(runs)
        elif result == "Walk":
            runs = self.advance_runners(1)
            self.bases[0] = True
            self.add_runs(runs)
    
    def add_runs(self, runs):
        """Add runs to the current batting team"""
        if self.top_bottom == "Top":
            self.away_score += runs
        else:
            self.home_score += runs
    
    def end_half_inning(self):
        """End the current half inning"""
        self.outs = 0
        self.bases = [False, False, False]
        
        if self.top_bottom == "Top":
            self.top_bottom = "Bottom"
        else:
            self.top_bottom = "Top"
            self.inning += 1
            
            # Check if game should end (9 innings)
            if self.inning > 9:
                self.game_over = True
    
    def play_inning(self):
        """Play a half inning"""
        while self.outs < 3 and not self.game_over:
            self.print_scoreboard()
            
            if self.top_bottom == "Top":
                print("Away team is batting...")
            else:
                print("Home team is batting...")
            
            input("Press Enter to swing the bat...")
            
            result = self.get_batting_result()
            self.handle_batting_result(result)
            
            time.sleep(1)
    
    def play_game(self):
        """Play the full baseball game"""
        print("Welcome to Baseball Game!")
        print("You are playing as the Home team.")
        print("The Away team will bat first.")
        
        while not self.game_over:
            self.play_inning()
        
        self.print_final_score()
    
    def print_final_score(self):
        """Print the final score and winner"""
        print("\n" + "="*50)
        print("GAME OVER!")
        print(f"FINAL SCORE: Away {self.away_score} - Home {self.home_score}")
        
        if self.home_score > self.away_score:
            print("🏆 HOME TEAM WINS! 🏆")
        elif self.away_score > self.home_score:
            print("🏆 AWAY TEAM WINS! 🏆")
        else:
            print("🤝 TIE GAME! 🤝")
        print("="*50)

def main():
    """Main function to run the baseball game"""
    game = BaseballGame()
    game.play_game()

if __name__ == "__main__":
    main()