from commentengine.serializers import MasterCommentSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from commentengine.models import MasterComment
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class MasterCommentList(APIView):
    parser_classes = (JSONParser,)



    def get(self, request, format=None):
        comments = MasterComment.objects.all()
        paginator = Paginator(comments, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            comments = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            comments = paginator.page(paginator.num_pages)

        serializer = MasterCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MasterCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterCommentDetail(APIView):
    """
    Retrieve, update or delete a comment instance.
    """
    parser_classes = (JSONParser,)

    def get_object(self, pk):
        try:
            return MasterComment.objects.get(pk=pk)
        except MasterComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment = MasterCommentSerializer(comment)
        return Response(comment.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = MasterCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChildDetailViewSet(viewsets.ModelViewSet):
    queryset = MasterComment.objects.all()
    serializer_class = MasterCommentSerializer
    filter_backends = (filters.SearchFilter,)
