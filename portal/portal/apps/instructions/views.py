
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Instruction


def instructions_view(request):
    all_instructions = Instruction.objects.all()
    return render(request, 'instrucrions.html', {'data': all_instructions})

def instruction_detail(request, instruction_id):
    instruction = get_object_or_404(Instruction, id=instruction_id)
    return render(request, 'instructions/instructions_detail.html', {'instruction': instruction})