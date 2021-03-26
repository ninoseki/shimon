<template>
  <nav
    role="navigation"
    aria-label="main navigation"
    class="navbar is-fixed-top"
  >
    <div class="navbar-brand">
      <a class="navbar-item"><h1 class="title">mmhdan</h1></a
      ><a role="button" aria-label="menu" class="navbar-burger burger"
        ><span aria-hidden="true"></span><span aria-hidden="true"></span
        ><span aria-hidden="true"></span
      ></a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start"></div>
      <div class="navbar-end">
        <a class="navbar-item"
          ><a href="/docs" target="_blank" class="navbar-item">API</a></a
        ><a class="navbar-item"
          ><a
            href="https://github.com/ninoseki/mmhdan"
            target="_blank"
            class="navbar-item"
            >GitHub</a
          ></a
        >
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  border-bottom: 1px solid lightgray;
}
</style>
