const name = 'alice'
const age = 23

const obj = {
  name,
  age,
  introduce() {
    console.log(`my Name is ${this.name}`)
    console.log(`my Age is ${this.age}`)
  }
}

export const some = '정의'
export { name, age, obj }