<script setup>
import { ref, onMounted } from "vue"

const message = ref("No data yet.")

const url = "/test-message"

async function fetchTestMessage() {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json()

    return result
  }
  catch (error) {
    return error.message
  }
}

onMounted(() => {
  fetchTestMessage().then(response => message.value = response)
})
</script>

<template>
  <h1>Result: {{ message }}</h1>
</template>

<style scoped></style>
