<script setup>
import { ref, onMounted } from "vue"

const data = ref("No data yet.")

const url = "http://localhost:5001/test-message"

async function fetchTestMessage() {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json()

    return result.data
  }
  catch (error) {
    return error.message
  }
}

onMounted(() => {
  fetchTestMessage().then(response => data.value = response)
})
</script>

<template>
  <div v-for="user in data">
    <h1>{{ user.name }}</h1>
    <h1>{{ user.age }}</h1>
    <hr>
  </div>
</template>

<style scoped></style>
