from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.table import Table
from rich import print

def main():
    print("[bold magenta]=== NHL Top scorers ===[/bold magenta]")

    while True:
        print("\nEnter season (eg: 2024-25): or [bold red]X[/bold red] to exit ")
        season = input().strip()

        if season.upper() == "X":
            break


        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        
        try:
            reader.get_players()
        except Exception:
            print(f"\n[bold red]Virhe:[/bold red] Could not fetch data for season: [bold]{season}[/bold]")
            continue
    
        nationalities = set(player.nationality for player in reader.get_players())
    
        print("[bold yellow]Available nationalities:[/bold yellow]")
        print(f"[dim green]{', '.join(nationalities)}[/dim green]")

        print("Enter nationality (eg: FIN, SWE, CAN) or [bold red]X[/bold red] to exit:")
        nationality = input().strip().upper()
        if nationality == "X":
            break


        players = stats.top_scorers_by_nationality(nationality)

        if not players:
            print(f"\n[bold red]Virhe:[/bold red] No players found for nationality: [bold]{nationality}[/bold]")
            continue

        table = Table(title=f"Top Scorers by Nationality {nationality} in {season}")
        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="left", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="yellow")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        print(table)

if __name__ == "__main__":
    main()
