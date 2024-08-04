from django.http import HttpResponse, JsonResponse
from .models import PlayerLevel


def assign_prize(request, player_level_id):
    try:
        player_level = PlayerLevel.objects.get(id=player_level_id)
        level_prize = player_level.assign_prize()
        return JsonResponse({'status': 'success', 'prize': level_prize.prize.title})
    except PlayerLevel.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'PlayerLevel does not exist'})
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def export_player_levels(request):
    response = PlayerLevel.export_to_csv()
    return response
