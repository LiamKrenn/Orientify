<script>
	import Compass from '$lib/Compass.svelte';

	let degree = 0;

	setInterval(() => {
		degree = (degree + 0.1) % 360;
	}, 2);
</script>

<Compass {degree} size={1} />
