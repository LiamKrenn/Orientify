<script lang="ts">
	import History from '$lib/History.svelte';
	import { onMount } from 'svelte';

	const steps = 10;
	let history_data: { [range: string]: number } = {};

	onMount(async () => {
		let res = await fetch('http://localhost:8002/orientation/grouped/?steps=' + steps);
		history_data = await res.json();
	});
</script>

{#if Object.keys(history_data).length > 0}
	<History {history_data} {steps} />
{/if}
