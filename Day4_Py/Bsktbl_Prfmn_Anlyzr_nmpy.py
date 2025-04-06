import numpy as np

np.random.seed(20)

performance = np.random.randint(10,41, size=(5,10))

print(performance)

avg_points = np.mean(performance, axis=1)
print("\nAverage points per game:")
print(np.round(avg_points, 1))

total_points = np.sum(performance, axis=1)
best_player = np.argmax(total_points)
worst_player = np.argmin(total_points)

print(f"\nBest-performing player: Player {best_player + 1} (Total: {total_points[best_player]} points)")
print(f"Worst-performing player: Player {worst_player + 1} (Total: {total_points[worst_player]} points)")

print("\n Games with scores above 30: ")
for i in range(performance.shape[0]):
    games = np.where(performance[i]>30)[0]+1
    if len(games)>0:
        clean_games = [int(g) for g in games] 
        print(f"Player {i + 1}:Games{clean_games}")
    else:
        print(f"Player {i + 1}: None")
        
sorted_indices = np.argsort(-total_points)
print("\nSorted Players by Total Points:", sorted_indices)

for rank, idx in enumerate(sorted_indices, 1):
    print(f"{rank}. Player {idx + 1} - {total_points[idx]} points")

