<script lang="ts">
	import { browser } from '$app/environment';
	import { PUBLIC_WS_URL } from '$env/static/public';
	import Compass from '$lib/Compass.svelte';
	import { onDestroy } from 'svelte';

	let degree = 0;

	let open = false;

	let noDataYet = true;
	let timePassed: string | null = null;
	let lastEventTime: number | null = null;

	let ws: WebSocket | null = null;

	if (!browser) {
		ws = new WebSocket(`${PUBLIC_WS_URL}`);

		ws.onopen = () => {
			open = true;
			console.log('Connected to WebSocket');
		};

		ws.onclose = () => {
			open = false;
			console.log('Disconnected from WebSocket');
		};

		ws.onmessage = (event) => {
			console.log(event);

			noDataYet = false;
			degree = parseFloat(event.data);
			lastEventTime = Date.now();
		};
	}

	setInterval(() => {
		if (lastEventTime) {
			const secondsPassed = Math.floor((Date.now() - lastEventTime) / 1000);
			const minutes = Math.floor(secondsPassed / 60);
			const seconds = secondsPassed % 60;
			if (minutes == 0 && seconds < 10) {
				timePassed = null;
			} else {
				timePassed = minutes > 0 ? `${minutes}m ${seconds}s` : `${seconds}s`;
			}
		}
	}, 1000);

	onDestroy(() => {
		ws?.close();
	});
</script>

{#if !open}
	<div class="absolute top-20 animate-pulse rounded-lg bg-red-600 p-4">
		Opening Live WebSocket...
	</div>
{:else}
	<div class="absolute top-20 rounded-lg bg-green-500/50 p-4">Connected</div>
{/if}

<div class="absolute mt-20 text-slate-500">
	{#if timePassed && !noDataYet}
		{timePassed}
	{/if}
	{#if open && noDataYet}
		No data yet
	{/if}
</div>

<Compass {degree} size={1} />
