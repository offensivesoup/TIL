import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([])

  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (todoId) {
    console.log(todoId)
    // todos 상태에서 인자로 전달된 todo(삭제 대상)을 찾아서 & 삭제를 한 새로운 배열을 반환
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    todos.value.splice(index, 1)
  }

  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodosCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true })
