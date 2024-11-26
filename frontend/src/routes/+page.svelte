<script>
	import Compass from '$lib/Compass.svelte';

	let degree = 0;

	setInterval(() => {
		degree = (degree + 0.1) % 360;
	}, 2);
</script>

<svelte:head>
	<title>Orientify</title>
</svelte:head>

<div class="flex h-full w-full items-center justify-center">
	<Compass {degree} size={1} />
</div>
