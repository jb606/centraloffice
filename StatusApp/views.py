from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django_tables2.views import SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render

from . import tables, filters, models, forms
# Create your views here.

def main_page(request):
    if request.user.is_authenticated:
        return redirect('/status/')
    else:
        return redirect('/accounts/login')

def GroupMembersList(request, slug):
    group = models.Group.objects.get(slug=slug)
    #members = group.members.order_by('user__last_name').all()
    current_user_slug = request.user.slug
    current_user = get_object_or_404(models.UserStatus, slug=current_user_slug)
    is_a_mod = False
    if current_user in group.mods.all():
        is_a_mod = True
    context = { 'group': group,
                'is_a_mod': is_a_mod,
     #           'members': members
               }
    return render(request, "StatusApp/grouplist.html", context=context)


def LoadGroupMembers(request, slug):
    group = models.Group.objects.get(slug=slug)
    members = group.members.order_by('user__last_name').all()
    context = { 
               'group': group,
               'members': members
               }
    return render(request, "StatusApp/partials/group_members.html", context=context)


def GroupModView(request, slug):
    group = models.Group.objects.get(slug=slug)
    current_user_slug = request.user.slug
    current_user = get_object_or_404(models.UserStatus, slug=current_user_slug)
    members = group.members.order_by('user__last_name').all()
    is_a_mod = False
    if current_user in group.mods.all():
        is_a_mod = True
    if not is_a_mod:
        return redirect('/status/')


    context = { 'group': group,
                'is_a_mod': is_a_mod,
                'members': members
               }
    return render(request, "StatusApp/group_admin.html", context=context)
def UserStatusModal(request, slug):
    user = models.UserStatus.objects.get(slug=slug)
    if request.method == "POST":
        form = forms.UserStatusForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            #return HttpResponse(status=204)
            response = HttpResponse(status=200)
            response['HX-Refresh'] = 'true'
            return response
    form = forms.UserStatusForm(instance=user)
    context = { 'user': user,
               'form': form}
    return render(request, "StatusApp/status_modal.html", context)
def CreateGroup(request, user_slug):
    if request.user.slug:
        current_user = models.UserStatus(slug=request.user.slug)
        group_name = request.GET.get('group', '')
        if group_name:
         new_group = models.Group(name=group_name)
         new_group.mods.add(current_user)
         new_group.members.add(current_user)
         new_group.save()
         GroupModView(request, new_group.slug)
         
    else:
        return redirect('/status/')
    
def GroupCRUD(request, slug, user, action):
    group = models.Group.objects.get(slug=slug)
    current_user_slug = request.user.slug
    current_user = get_object_or_404(models.UserStatus, slug=current_user_slug)
    user_object = get_object_or_404(models.UserStatus, slug=user)
    is_a_mod = False
    if current_user in group.mods.all():
        is_a_mod = True
    if not is_a_mod:
        return redirect('/status/')

    admin_mode=True
    context = { 'group': group,
                'is_a_mod': is_a_mod,
                'admin_mode': admin_mode,

               }
    members = group.members.order_by('user__last_name').all()
    context['members'] = members
    match action:
        case "admin_mode":
            return render(request, "StatusApp/partials/group_members.html", context)

        case "addmember":
            group.members.add(user_object)
            group = models.Group.objects.get(slug=slug)
            members = group.members.order_by('user__last_name').all()
            context['members'] = members
            return render(request, "StatusApp/partials/group_members.html", context)

        case "deletemember":
            group.members.remove(user_object)
            group = models.Group.objects.get(slug=slug)
            members = group.members.order_by('user__last_name').all()
            context['members'] = members
            return render(request, "StatusApp/partials/group_members.html", context)

        case "addmod":
            group.mods.add(user_object)
            group = models.Group.objects.get(slug=slug)
            members = group.members.order_by('user__last_name').all()
            return render(request, "StatusApp/partials/group_members.html", context)
        
        case "deletemod":
            group.mods.remove(user_object)
            group = models.Group.objects.get(slug=slug)
            members = group.members.order_by('user__last_name').all()
            return render(request, "StatusApp/partials/group_members.html", context)

        case _:
            return redirect('/status/')
    return redirect('/status/')

def UserSearch(request, slug):
    group = models.Group.objects.get(slug=slug)
    context = {'group': group}
    searchstr = request.GET.get('search', '')
    users = ''
    if searchstr:
        users = models.UserStatus.objects.filter(Q(user__first_name__icontains=searchstr) |
                                                 Q(user__username__icontains=searchstr) |
                                                 Q(user__last_name__icontains=searchstr)
                                                   ).distinct().exclude(member_of=group)
    print("---")
    for u in users:
        print(u)
    print("---")
    context['users'] = users
    
    return render(request, "StatusApp/partials/search.html", context)



def UpdateUserStatus(request, user_slug, status_slug ):
    user = get_object_or_404(models.UserStatus, slug=user_slug)
    status = get_object_or_404(models.Status, slug=status_slug)
    user.status = status
    user.save()
    return HttpResponse(status=204)

    pass
    #user = models.UserStatus.get(slug=user_slug)



class GroupListView(SingleTableMixin, FilterView):
    model = models.Group
    template_name = "StatusApp/sb_filter.html"
    table_class = tables.GroupTable
    filterset_class = filters.GroupFilter
    table_pagination = {
        "per_page": 25,
    }

class GroupView(SingleTableMixin, DetailView):
    model = models.Group
    template_name = "StatusApp/sb_group.html"
    table_class = tables.GroupTable
    form_class = forms.GroupForm



