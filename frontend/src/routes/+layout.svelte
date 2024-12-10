<script lang="ts">
	import { page } from '$app/stores';
	import '../app.css';
</script>

<div class="absolute left-4 top-4 flex items-center">
	<h1 class="mr-2 text-4xl font-bold">Orientify</h1>
	<a
		class="ml-4 text-2xl underline-offset-[6px] {$page.url.pathname == '/' ? 'underline' : ''}"
		href="/"
	>
		Live
	</a>
	<a
		class="ml-4 text-2xl underline-offset-[6px] {$page.url.pathname == '/history'
			? 'underline'
			: ''}"
		href="/history"
	>
		History
	</a>
</div>

<svelte:head>
	<title>Orientify</title>
</svelte:head>

<div class="flex h-full w-full items-center justify-center">
	<slot />
</div>
