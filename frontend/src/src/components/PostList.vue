<template>
    <div class="post-list">
        <ul class="post-list-ul">
            <li v-for="post in posts" :key="post.id" class="post-item">
                <div class="post-content">
                  <div class="post-title">
                    <h2>Номер {{ post.id }} Текст: {{ post.title }}</h2>
                  </div>
                  <div class="post-body">
                    <p>Текст поста: {{ post.body }}</p>
                  </div>
                  <div class="post-date">
                    <p>Дата создания: {{ formatDate(post.created_at) }}</p>
                  </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
body {
  background-color: antiquewhite;
  color: darkslategray;
  margin: 0;
  padding: 0;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html, body {
  height: 100%;
}
.post-list:after,
.post-item:after {
  content: "";
  display: table;
  clear: both;
}

.post-list-ul {
    list-style: none;
    margin: 0;
    padding: 0;
}
.post-list {
  max-width: 1200px;
  margin: 0 auto;
}

.post-item {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 10px;
  box-sizing: border-box;
}

.post-content {
  border: 1px solid #ddd;
  padding: 10px;
}

.post-title {
  border-bottom: 2px solid #ddd; /* Стиль границы для заголовка */
  padding: 10px;
  text-align: center;
}

.post-body {
  max-width: 100%;
  font-size: 16px; /* Базовый размер шрифта */
  border: 1px solid #ccc; /* Стиль границы для текста поста */
  padding: 10px;
  box-sizing: border-box;
}

.post-date {
  text-align: center; /* Центрируем текст */
  color: #4a4ab3; /* Цвет текста синий */
  text-shadow: 1px 1px 2px rgba(20, 20, 121, 0.5); /* Тень текста синего цвета */
  /* Другие стили, если необходимо */
}
/* Медиа-запрос для адаптации на планшетах */
@media screen and (max-width: 768px) {
  .post-item {
    width: 100%;
    max-width: none;
  }
}

/* Медиа-запрос для адаптации на мобильных устройствах */
@media screen and (max-width: 480px) {
  .post-content {
    padding: 5px;
  }
}
</style>

<script>
export default {
  props: {
    posts: {
      type: Array,
      default: () => [],
    },
    post: {
      type: Object,
    },
  },
  // Используйте методы вместо фильтров
  methods: {
    formatDate(value) {
      const dateObject = new Date(value);
      const year = dateObject.getFullYear();
      const month = (dateObject.getMonth() + 1).toString().padStart(2, '0');
      const day = dateObject.getDate().toString().padStart(2, '0');
      const hours = dateObject.getHours().toString().padStart(2, '0');
      const minutes = dateObject.getMinutes().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}`;
    },
  },
};
</script>
