<script lang="ts">
	import { PUBLIC_DB_URL } from '$env/static/public';
	import History from '$lib/History.svelte';
	import { onMount } from 'svelte';

	const steps = 10;
	let history_data: { [range: string]: number } = {};

	onMount(async () => {
		let res = await fetch(`${PUBLIC_DB_URL}/orientation/grouped/?steps=` + steps);
		history_data = await res.json();
	});
</script>

{#if Object.keys(history_data).length > 0}
	<History {history_data} {steps} />
{/if}
