import csv

from django.db import models
from django.http import HttpResponse
from django.utils import timezone


class Player(models.Model):
    player_id = models.CharField(max_length=100)


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField(max_length=100)  # указываем max_length для CharField


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def assign_prize(self):
        if self.is_completed:
            prize = Prize.objects.first()
            level_prize = LevelPrize.objects.create(level=self.level, prize=prize, received=timezone.now())
            return level_prize
        else:
            raise ValueError("Level is not completed yet")

    @staticmethod
    def export_to_csv():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'

        writer = csv.writer(response)
        writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Prize Title'])

        for player_level in PlayerLevel.objects.select_related('player', 'level').all():
            level_prize = LevelPrize.objects.filter(level=player_level.level).first()
            prize_title = level_prize.prize.title if level_prize else 'No Prize'
            writer.writerow([player_level.player.player_id, player_level.level.title, player_level.is_completed, prize_title])

        return response


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField(null=True, blank=True)
