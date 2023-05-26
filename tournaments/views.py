from django.shortcuts import render, redirect, get_object_or_404
from .models import Tournament, Team, Match, Registration
from .forms import TeamForm, MatchResultForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournament_list.html', {'tournaments': tournaments})


@login_required
def register_team(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            form.save_m2m()

            Registration.objects.create(tournament=tournament, team=team)

            return redirect('tournament_detail', tournament_id=tournament_id)
    else:
        form = TeamForm()

    return render(request, 'register_team.html', {'tournament': tournament, 'form': form})


def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    return render(request, 'tournament_detail.html', {'tournament': tournament})


@login_required
def add_match_result(request, match_id):
    match = get_object_or_404(Match, id=match_id)

    if request.method == 'POST':
        form = MatchResultForm(request.POST)
        if form.is_valid():
            winner = form.cleaned_data['winner']
            match.winner = winner
            match.save()

            return redirect('tournament_detail', tournament_id=match.tournament.id)
    else:
        form = MatchResultForm()

    return render(request, 'add_match_result.html', {'match': match, 'form': form})


@login_required
def dashboard(request):  # tylko zalogowani
    return render(request, 'dashboard.html')
