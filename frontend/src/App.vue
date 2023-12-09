<template>
    <header>
        <div className="wrapper">
        </div>
    </header>

    <div id="app">
        <div className="content">
            <AddPostForm @addPost="addPost"/>
            <PostList :posts="posts"/>
        </div>
    </div>
</template>

<script>
import PostList from "@/components/PostList.vue";
import AddPostForm from "@/components/AddPostForm.vue";

export default {

    data() {
        return {
            baseUrl: "http://192.168.181.135:8000",
            posts: [],
        };
    },
    created() {
        this.fetchPosts();
    },
    methods: {

        fetchPosts() {
            fetch(`${this.baseUrl}/api/posts/`)
                .then((response) => response.json())
                .then((data) => {
                    this.posts = data;
                })
                .catch((error) => {
                    console.error("Error fetching posts:", error);
                });
            window.scrollTo({top: 0, behavior: 'smooth'});
        },
        addPost(postTitle, postBody) {
            fetch(`${this.baseUrl}/api/create-post/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.getCookie("csrftoken"),
                },
                body: JSON.stringify({
                    user: "1",
                    title: postTitle,
                    body: postBody,
                }),
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(() => {
                    this.fetchPosts(); // Обновляем список после добавления нового поста
                })
                .catch((error) => {
                    console.error("Error adding post:", error);
                });
        },
        getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(";").shift();
        },
    },
    components: {
        PostList,
        AddPostForm,
    },
};

// const posts = ref([]);
// const fetchPosts = async () => {
//     try {
//         const response = await fetch("http://192.168.181.135:8000/api/posts/");
//         const data = await response.json();
//         posts.value = data;
//         console.log('posts', posts)
//     } catch (error) {
//         console.error("Error fetching posts:", error);
//     }
//};

// const addPost = async (title, body) => {
//     try {
//         const response = await fetch("http://192.168.181.135:8000/api/create-post/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "X-CSRFToken": getCookie("csrftoken"),
//             },
//             body: JSON.stringify({
//                 user: "1",
//                 title: title,
//                 body: body,
//             }),
//         });
//
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//
//         await response.json();
//         fetchPosts();
//
//     } catch (error) {
//         console.error("Error adding post:", error);
//     }
// };

// const getCookie = (name) => {
//     const value = `; ${document.cookie}`;
//     const parts = value.split(`; ${name}=`);
//     if (parts.length === 2) return parts.pop().split(";").shift();
// };
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
</script>


<style scoped>
/**/
header {
    line-height: 1.5;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}
</style>
