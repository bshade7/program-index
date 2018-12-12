from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Program
from .forms import ProgramForm


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program/program_list.html', {'programs': programs})


def save_program_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            programs = Program.objects.all()
            data['html_program_list'] = render_to_string('programs/includes/partial_program_list.html', {
                'programs': programs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
    else:
        form = ProgramForm()
    return save_program_form(request, form, 'programs/includes/partial_program_create.html')


def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
    else:
        form = ProgramForm(instance=program)
    return save_program_form(request, form, 'programs/includes/partial_program_update.html')


def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    data = dict()
    if request.method == 'POST':
        program.delete()
        data['form_is_valid'] = True
        programs = Program.objects.all()
        data['html_program_list'] = render_to_string('programs/includes/partial_program_list.html', {
            'programs': programs
        })
    else:
        context = {'program': program}
        data['html_form'] = render_to_string('programs/includes/partial_program_delete.html', context, request=request)
    return JsonResponse(data)
