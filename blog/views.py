from django.shortcuts import render
from django.http import HttpResponse

all_posts = [
    dict(
        title="Post 1",
        summary="This is the summary of post 1",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum gravida lacus enim, eget dictum nisl vulputate non. Curabitur non luctus nunc. Phasellus dui tellus, ultrices quis dignissim vel, ornare at mauris. Fusce imperdiet consequat est, et sagittis purus bibendum et. Donec molestie quis lacus sit amet bibendum. Proin rutrum urna ex, sed ornare leo vestibulum et. Donec scelerisque magna nec risus iaculis elementum non in sem. Vestibulum rutrum mollis ligula, et ornare neque bibendum vel. Nullam faucibus leo eu tortor feugiat bibendum. Mauris nibh arcu, tristique eu nisi a, egestas condimentum turpis. Donec massa orci, posuere et diam auctor, feugiat luctus est. In hac habitasse platea dictumst. Maecenas varius ex et justo lobortis vestibulum. Curabitur lobortis, libero nec volutpat pellentesque, dui est posuere lectus, eget venenatis risus tortor vel nibh. Quisque ut orci nibh. Pellentesque sodales eros libero, vel eleifend lectus auctor nec. Fusce sem leo, mollis vitae dapibus eget, egestas aliquam est. Vivamus massa orci, auctor imperdiet dapibus sed, egestas id leo. Mauris condimentum felis erat, sed interdum metus semper a. Suspendisse nisl sapien, lacinia quis efficitur non, iaculis eget lacus. Nulla mattis lobortis odio, ut iaculis urna tincidunt vitae. Vivamus dictum enim eu libero mollis, vel gravida eros efficitur. Sed auctor dui nec vehicula euismod. Vivamus non fringilla tortor, id blandit dui.",
        slug="post-1"
    ),
    dict(
        title="Post 2",
        summary="This is the summary of post 2",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum gravida lacus enim, eget dictum nisl vulputate non. Curabitur non luctus nunc. Phasellus dui tellus, ultrices quis dignissim vel, ornare at mauris. Fusce imperdiet consequat est, et sagittis purus bibendum et. Donec molestie quis lacus sit amet bibendum. Proin rutrum urna ex, sed ornare leo vestibulum et. Donec scelerisque magna nec risus iaculis elementum non in sem. Vestibulum rutrum mollis ligula, et ornare neque bibendum vel. Nullam faucibus leo eu tortor feugiat bibendum. Mauris nibh arcu, tristique eu nisi a, egestas condimentum turpis. Donec massa orci, posuere et diam auctor, feugiat luctus est. In hac habitasse platea dictumst. Maecenas varius ex et justo lobortis vestibulum. Curabitur lobortis, libero nec volutpat pellentesque, dui est posuere lectus, eget venenatis risus tortor vel nibh. Quisque ut orci nibh. Pellentesque sodales eros libero, vel eleifend lectus auctor nec. Fusce sem leo, mollis vitae dapibus eget, egestas aliquam est. Vivamus massa orci, auctor imperdiet dapibus sed, egestas id leo. Mauris condimentum felis erat, sed interdum metus semper a. Suspendisse nisl sapien, lacinia quis efficitur non, iaculis eget lacus. Nulla mattis lobortis odio, ut iaculis urna tincidunt vitae. Vivamus dictum enim eu libero mollis, vel gravida eros efficitur. Sed auctor dui nec vehicula euismod. Vivamus non fringilla tortor, id blandit dui.",
        slug="post-2"
    ),
    dict(
        title="Post 3",
        summary="This is the summary of post 3",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum gravida lacus enim, eget dictum nisl vulputate non. Curabitur non luctus nunc. Phasellus dui tellus, ultrices quis dignissim vel, ornare at mauris. Fusce imperdiet consequat est, et sagittis purus bibendum et. Donec molestie quis lacus sit amet bibendum. Proin rutrum urna ex, sed ornare leo vestibulum et. Donec scelerisque magna nec risus iaculis elementum non in sem. Vestibulum rutrum mollis ligula, et ornare neque bibendum vel. Nullam faucibus leo eu tortor feugiat bibendum. Mauris nibh arcu, tristique eu nisi a, egestas condimentum turpis. Donec massa orci, posuere et diam auctor, feugiat luctus est. In hac habitasse platea dictumst. Maecenas varius ex et justo lobortis vestibulum. Curabitur lobortis, libero nec volutpat pellentesque, dui est posuere lectus, eget venenatis risus tortor vel nibh. Quisque ut orci nibh. Pellentesque sodales eros libero, vel eleifend lectus auctor nec. Fusce sem leo, mollis vitae dapibus eget, egestas aliquam est. Vivamus massa orci, auctor imperdiet dapibus sed, egestas id leo. Mauris condimentum felis erat, sed interdum metus semper a. Suspendisse nisl sapien, lacinia quis efficitur non, iaculis eget lacus. Nulla mattis lobortis odio, ut iaculis urna tincidunt vitae. Vivamus dictum enim eu libero mollis, vel gravida eros efficitur. Sed auctor dui nec vehicula euismod. Vivamus non fringilla tortor, id blandit dui.",
        slug="post-3"
    ),
]


def index(request):

    context = dict()

    return render(request, "blog/index.html", context)


def get_all_posts(request):

    context = dict(
        posts=all_posts
    )

    return render(request, "blog/all_posts.html", context)


def get_posts_by_slug(request, slug):

    post = [p for p in all_posts if p["slug"] == slug]

    context = dict(
        post=post[0]
    )

    return render(request, "blog/post.html", context)
