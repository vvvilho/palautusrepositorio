from rich.table import Table
from rich import print as rprint

from player_reader import PlayerReader
from player_stats import PlayerStats


def ask_season():
    rprint("\nEnter season (eg: 2024-25): or [bold red]X[/bold red] to exit ")
    return input().strip()


def ask_nationality():
    rprint("Enter nationality (eg: FIN, SWE, CAN) or [bold red]X[/bold red] to exit:")
    return input().strip().upper()


def fetch_players(season, reader):
    try:
        return reader.get_players()
    except Exception:   # pylint: disable=broad-except
        rprint(f"\n[bold red]Virhe:[/bold red] Could not fetch data for season: [bold]{season}[/bold]")
        return None


def print_nationalities(players):
    nationalities = set(player.nationality for player in players)

    rprint("[bold yellow]Available nationalities:[/bold yellow]")
    rprint(f"[dim green]{', '.join(nationalities)}[/dim green]")


def player_table(nationality, season):
    table = Table(title=f"Top Scorers by {nationality} in {season}")
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="yellow")
    return table


def add_players_to_table(table, players):
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))


def print_players(players, nationality, season):
    table = player_table(nationality, season)
    add_players_to_table(table, players)
    rprint(table)


def ask_view():
    rprint("Choose view: [bold]N[/bold] = Nationality, [bold]T[/bold] = Team or [bold red]X[/bold red] to exit:")
    return input().strip().upper()


def ask_team():
    rprint("Enter team (eg: BOS, NYR) or [bold red]X[/bold red] to exit:")
    return input().strip().upper()

def print_teams(players):
    teams = {
        team.strip().upper()
        for player in players
        if player.team
        for team in player.team.split(",")
    }

    for team in sorted(teams):
        print(team)

    rprint("[bold yellow]Available teams:[/bold yellow]")
    rprint(f"[dim green]{', '.join(sorted(teams))}[/dim green]")


def stats_for_season(season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    return reader, PlayerStats(reader)


def top_scorers_by_nationality(stats, nationality):
    top_scorers = stats.top_scorers_by_nationality(nationality)

    if not top_scorers:
        rprint(f"\n[bold red]Virhe:[/bold red] No players found for nationality: [bold]{nationality}[/bold]")

    return top_scorers


def handle_nationality_flow(players, stats, season):
    """Handle the nationality view flow. Return True to continue, False to exit."""
    print_nationalities(players)
    nationality = ask_nationality()
    if nationality == "X":
        return False

    top_scorers = top_scorers_by_nationality(stats, nationality)
    if not top_scorers:
        return True

    print_players(top_scorers, nationality, season)
    return True


def handle_team_flow(players, stats, season):
    """Handle the team view flow. Return True to continue, False to exit."""
    print_teams(players)
    team = ask_team()
    if team == "X":
        return False

    top_scorers = stats.top_scorers_by_team(team)
    if not top_scorers:
        rprint(f"\n[bold red]Virhe:[/bold red] No players found for team: [bold]{team}[/bold]")
        return True

    print_players(top_scorers, team, season)
    return True


def handle_season(season):
    reader, stats = stats_for_season(season)
    players = fetch_players(season, reader)

    if players is None:
        return True

    view = ask_view()
    if view == "N":
        return handle_nationality_flow(players, stats, season)
    if view == "T":
        return handle_team_flow(players, stats, season)
    if view == "X":
        return False

    rprint("[bold red]Invalid option[/bold red]")
    return True


def main():
    rprint("[bold magenta]=== NHL Top scorers ===[/bold magenta]")

    while True:
        season = ask_season()

        if season.upper() == "X":
            break

        if not handle_season(season):
            break

if __name__ == "__main__":
    main()
