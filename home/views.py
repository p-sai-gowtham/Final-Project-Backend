from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets
from django.db.models import Q


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        search = self.request.query_params.get("search")
        type_filter = self.request.query_params.get("type")
        status_filter = self.request.query_params.get("status")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(client__icontains=search)
            )

        if type_filter:
            queryset = queryset.filter(type=type_filter)

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        sort_field = self.request.query_params.get("ordering")
        if sort_field:
            queryset = queryset.order_by(sort_field)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
