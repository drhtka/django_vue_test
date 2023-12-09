<template>
    <form @submit.prevent="addPost" class="post-form">
        <label for="postTitle">Заголовок поста:</label>
        <input v-model="postTitle" type="text" id="postTitle" name="postTitle" required />
        <label for="postBody">Текст поста:</label>
        <textarea v-model="postBody" id="postBody" name="postBody" required></textarea>
        <button type="submit">Добавить пост</button>
    </form>
</template>
<style scoped>
.post-form {
    display: flex;
    flex-direction: column;
    max-width: 400px; /* Пример максимальной ширины формы */
    margin: 0 auto;  /* Центрирование формы */
}

label {
    margin-bottom: 8px;
}

input, textarea {
    margin-bottom: 16px;
    padding: 8px;
}

button {
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
<script>
export default {
    data() {
        return {
            postTitle: '',
            postBody: '',
        };
    },
    methods: {
        addPost() {
            if (this.postTitle.trim() !== '' && this.postBody.trim() !== '') {
                this.$emit('addPost', this.postTitle.trim(), this.postBody.trim());
                this.postTitle = '';
                this.postBody = '';
            }
        },
    },
};
</script>
