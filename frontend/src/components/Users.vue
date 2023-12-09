<script setup>
defineProps({
    msg: {
        type: String,
        required: true
    }
})
</script>

<template>
    <h3> Users:</h3>
</template>

<script>
export default {
    name: 'Users',
}
</script>

<style>
h3 {
    margin-bottom: 5%;
}
</style>
