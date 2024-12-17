<script>
	import { PUBLIC_WS_IP, PUBLIC_WS_PORT } from '$env/static/public';
	import Compass from '$lib/Compass.svelte';

	let degree = 0;

	let open = false;

	let ws = new WebSocket(`ws://${PUBLIC_WS_IP}:${PUBLIC_WS_PORT}/`);

	ws.onopen = () => {
		open = true;
		console.log('Connected to WebSocket');
	};

	ws.onmessage = (event) => {
		console.log(event);

		degree = parseFloat(event.data);
	};

	// setInterval(() => {
	// 	degree = (degree + 0.1) % 360;
	// }, 2);
</script>

{#if !open}
	<div class="absolute top-20 animate-pulse rounded-lg bg-red-600 p-4">
		Opening Live WebSocket...
	</div>
{:else}
	<div class="absolute top-20 rounded-lg bg-green-500/50 p-4">Connected</div>
{/if}

<Compass {degree} size={1} />
