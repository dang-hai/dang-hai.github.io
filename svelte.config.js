import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { mdsvex } from 'mdsvex';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [vitePreprocess(), mdsvex()],

	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: 'index.html',
			precompress: false,
			strict: true
		}),
		paths: {
			base: ''
		},
		appDir: 'app',
		prerender: {
			handleHttpError: ({ path, referrer, message }) => {
				if (path === '/not-found') {
					return;
				}

				throw new Error(message);
			}
		}
	},

	extensions: ['.svelte', '.svx']
};

export default config;
